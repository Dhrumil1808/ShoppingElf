package com.example.adityaparmar.shoppingelf_v_10;

import android.app.DatePickerDialog;
import android.content.ActivityNotFoundException;
import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.net.Uri;
import android.os.Bundle;
import android.os.Environment;
import android.provider.MediaStore;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.DatePicker;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.ImageView;

import com.example.adityaparmar.shoppingelf_v_10.service.UploadImageClient;

import java.io.File;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import java.util.Locale;

import okhttp3.MediaType;
import okhttp3.MultipartBody;
import okhttp3.OkHttpClient;
import okhttp3.RequestBody;
import okhttp3.ResponseBody;
import okhttp3.logging.HttpLoggingInterceptor;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class UploadReceiptActivity extends AppCompatActivity {
    private static final int ACTIVITY_START_CAMERA_APP = 0;
    private static final int CROPING_CODE = 1;
    private ImageView mPhotoCapturedImageView;
    private String mImageFileLocation = "";
    Intent CropIntent;
    Uri mImageCaptureUri;
    Calendar myCalendar = Calendar.getInstance();
    ImageButton ibCalender;
    private EditText billdate;
    int b_day,b_month,b_year;
    static final int Dialog_ID=55;

    UploadImageClient service;
    File imageservicepath;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_upload_receipt);

        mPhotoCapturedImageView = (ImageView) findViewById(R.id.capturePhotoImageView);

        //Back Button

        this.getSupportActionBar().setDisplayHomeAsUpEnabled(true);

        //open camera

        takePhoto();

        // select Date Event

        ibCalender = (ImageButton)findViewById(R.id.ibcalender);
        ibCalender.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                new DatePickerDialog(UploadReceiptActivity.this, date, myCalendar
                        .get(Calendar.YEAR), myCalendar.get(Calendar.MONTH),
                        myCalendar.get(Calendar.DAY_OF_MONTH)).show();



            }
        });

        //services

        HttpLoggingInterceptor interceptor = new HttpLoggingInterceptor();
        interceptor.setLevel(HttpLoggingInterceptor.Level.BODY);
        OkHttpClient client = new OkHttpClient.Builder().addInterceptor(interceptor).build();

        // Change base URL to your upload server URL.
        //service = new Retrofit.Builder().baseUrl("http://54.241.140.236:3009").client(client).build().create(UploadImageClient.class);


    }
    DatePickerDialog.OnDateSetListener date = new DatePickerDialog.OnDateSetListener() {

        @Override
        public void onDateSet(DatePicker view, int year, int monthOfYear,
                              int dayOfMonth) {
            // TODO Auto-generated method stub
            myCalendar.set(Calendar.YEAR, year);
            myCalendar.set(Calendar.MONTH, monthOfYear);
            myCalendar.set(Calendar.DAY_OF_MONTH, dayOfMonth);
            updateLabel();
        }

    };
    private void updateLabel() {

        billdate = (EditText)findViewById(R.id.billdate);
        String myFormat = "MM/dd/yyyy"; //In which you need put here
        SimpleDateFormat sdf = new SimpleDateFormat(myFormat, Locale.US);

        billdate.setText(sdf.format(myCalendar.getTime()));
        //Toast.makeText(this,(sdf.format(myCalendar.getTime())).toString(),Toast.LENGTH_LONG).show();
    }

    public void takePhoto() {
        Intent callCameraApplicationIntent = new Intent();
        callCameraApplicationIntent.setAction(MediaStore.ACTION_IMAGE_CAPTURE);

        File photoFile = null;
        try {
            photoFile = createImageFile();

        } catch (IOException e) {
            e.printStackTrace();
        }
        callCameraApplicationIntent.putExtra(MediaStore.EXTRA_OUTPUT, Uri.fromFile(photoFile));

        startActivityForResult(callCameraApplicationIntent, ACTIVITY_START_CAMERA_APP);
    }
    public void takePhoto(View view) {
        Intent callCameraApplicationIntent = new Intent();
        callCameraApplicationIntent.setAction(MediaStore.ACTION_IMAGE_CAPTURE);

        File photoFile = null;
        try {
            photoFile = createImageFile();

        } catch (IOException e) {
            e.printStackTrace();
        }
        callCameraApplicationIntent.putExtra(MediaStore.EXTRA_OUTPUT, Uri.fromFile(photoFile));

        startActivityForResult(callCameraApplicationIntent, ACTIVITY_START_CAMERA_APP);
    }

    protected void onActivityResult (int requestCode, int resultCode, Intent data) {
        if(requestCode == ACTIVITY_START_CAMERA_APP && resultCode == RESULT_OK) {
            // Toast.makeText(this, "Picture taken successfully", Toast.LENGTH_SHORT).show();
            // Bundle extras = data.getExtras();
            // Bitmap photoCapturedBitmap = (Bitmap) extras.get("data");
            // mPhotoCapturedImageView.setImageBitmap(photoCapturedBitmap);
            // Bitmap photoCapturedBitmap = BitmapFactory.decodeFile(mImageFileLocation);
            // mPhotoCapturedImageView.setImageBitmap(photoCapturedBitmap);

            //setReducedImageSize();
            CropingIMG();

        }
        else if (requestCode == CROPING_CODE && resultCode == RESULT_OK)
        {
            setReducedImageSize();
        }
    }
    File createImageFile() throws IOException {

        String timeStamp = new SimpleDateFormat("yyyyMMdd_HHmmss").format(new Date());
        String imageFileName = "IMAGE_" + timeStamp + "_";
        File storageDirectory = Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_PICTURES);

        File image = File.createTempFile(imageFileName,".jpg", storageDirectory);
        imageservicepath =image;
        mImageFileLocation = image.getAbsolutePath();
        mImageCaptureUri = Uri.fromFile(image);
        return image;

    }

    void setReducedImageSize() {
        int targetImageViewWidth = mPhotoCapturedImageView.getWidth();
        int targetImageViewHeight = mPhotoCapturedImageView.getHeight();

        BitmapFactory.Options bmOptions = new BitmapFactory.Options();
        bmOptions.inJustDecodeBounds = true;
        BitmapFactory.decodeFile(mImageFileLocation, bmOptions);
        int cameraImageWidth = bmOptions.outWidth;
        int cameraImageHeight = bmOptions.outHeight;

        int scaleFactor = Math.min(cameraImageWidth/targetImageViewWidth, cameraImageHeight/targetImageViewHeight);
        bmOptions.inSampleSize = scaleFactor;
        bmOptions.inJustDecodeBounds = false;

        Bitmap photoReducedSizeBitmp = BitmapFactory.decodeFile(mImageFileLocation, bmOptions);
        mPhotoCapturedImageView.setImageBitmap(photoReducedSizeBitmp);


    }
    private void CropingIMG() {

        try{
            CropIntent = new Intent("com.android.camera.action.CROP");
            CropIntent.setDataAndType(mImageCaptureUri,"image/*");

            CropIntent.putExtra("crop","true");
            CropIntent.putExtra("outputX",360);
            CropIntent.putExtra("outputY",360);
            //CropIntent.putExtra("aspectX",1);
            //CropIntent.putExtra("aspectY",1);
            CropIntent.putExtra("scaleUpIfNeeded",true);
            CropIntent.putExtra("return-data",true);

            startActivityForResult(CropIntent,CROPING_CODE);
        }
        catch (ActivityNotFoundException ex)
        {

        }

    }

    public void uploadimage(View view)
    {
        File fileimage = imageservicepath;
        billdate = (EditText)findViewById(R.id.billdate);



        String myFormat = "yyyy/MM/dd"; //In which you need put here
        SimpleDateFormat sdf = new SimpleDateFormat(myFormat, Locale.US);

        String bill_date = (sdf.format(myCalendar.getTime()));

       // Toast.makeText(this,bill_date, Toast.LENGTH_LONG).show();



        RequestBody mFile = RequestBody.create(MediaType.parse("multipart/form-data"), fileimage);
        MultipartBody.Part fileToUpload = MultipartBody.Part.createFormData("file", fileimage.getName(), mFile);
        RequestBody rbbilldate = RequestBody.create(MediaType.parse("multipart/form-data"), bill_date);
        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl("http://54.241.140.236:3009")
                .addConverterFactory(GsonConverterFactory.create())
                .build();
        UploadImageClient uploadImage = retrofit.create(UploadImageClient.class);
        Call<ResponseBody> fileUpload = uploadImage.postImage(fileToUpload, rbbilldate);
        fileUpload.enqueue(new Callback<ResponseBody>() {
            @Override
            public void onResponse(Call<ResponseBody> call, Response<ResponseBody> response) {
               // Toast.makeText(UploadReceiptActivity.this, "Response " + response.raw().message(), Toast.LENGTH_LONG).show();
                //Toast.makeText(UploadReceiptActivity.this, "Success " + response.body().getSuccess(), Toast.LENGTH_LONG).show();
            }
            @Override
            public void onFailure(Call<ResponseBody> call, Throwable t) {
                //Log.d(TAG, "Error " + t.getMessage());
            }
        });
        }

    }



/*

    References:https://github.com/mobapptuts/camera_intent

 */