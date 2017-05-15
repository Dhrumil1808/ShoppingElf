package com.example.adityaparmar.shoppingelf_v_10;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

import com.example.adityaparmar.shoppingelf_v_10.model.MySignInRequest;
import com.example.adityaparmar.shoppingelf_v_10.model.MySignInResponse;
import com.example.adityaparmar.shoppingelf_v_10.service.ProfileClient;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class ProfileActivity extends AppCompatActivity {

    EditText txtemail;
    EditText txtpassword;
    //EditText txtfamilymember;
    EditText txt;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_profile);

        this.getSupportActionBar().setDisplayHomeAsUpEnabled(true);

        txtemail = (EditText)findViewById(R.id.txtprofilemail);
        txtpassword=(EditText)findViewById(R.id.txtprofilpassword);
        //txtfamilymember=(EditText)findViewById(R.id.txtprofilfamilymembers);

        SharedPreferences sharedPreferences = getSharedPreferences("logindata", Context.MODE_PRIVATE);
        String email = sharedPreferences.getString("email","");
        String password = sharedPreferences.getString("password","");

        txtemail.setText(email);
        txtpassword.setText(password);



    }

    public  void updatedata(View view){
        if(checkvalidation()){

            final String email = txtemail.getText().toString();
            final String password = txtpassword.getText().toString();



            MySignInRequest mySignInRequest = new MySignInRequest();
            mySignInRequest.setEmail(email);
            mySignInRequest.setPassword(password);


            Retrofit retrofit = new Retrofit.Builder()
                    .baseUrl("http://54.241.140.236:3009")
                    .addConverterFactory(GsonConverterFactory.create())
                    .build();



            //SignUpClient signUpClient = retrofit.create(SignUpClient.class);

            ProfileClient profileClient = retrofit.create(ProfileClient.class);


            Call<MySignInResponse> callsignin = profileClient.checkuser(mySignInRequest);




            callsignin.enqueue(new Callback<MySignInResponse>() {
                @Override
                public void onResponse(Call<MySignInResponse> call, Response<MySignInResponse> response) {
                    //Snackbar.make(findViewById(R.id.main_content), "Account created Successfully",Snackbar.LENGTH_LONG).show();

                    String ch = "ACCESS_DENIED";
                    if(ch.equals(response.body().getMessage())){

                        Toast.makeText(ProfileActivity.this,response.body().getMessage(), Toast.LENGTH_LONG).show();

                    }else
                    {
                        Toast.makeText(ProfileActivity.this,response.body().getMessage(), Toast.LENGTH_LONG).show();

                        setsharedpreference(email,password);

                        Intent i = new Intent(ProfileActivity.this,MainActivity.class);
                        startActivity(i);
                    }





                }

                @Override
                public void onFailure(Call<MySignInResponse> call, Throwable t) {
                    Snackbar.make(findViewById(R.id.rllogin), "Something went wrong !!",Snackbar.LENGTH_LONG).show();

                }
            });



        }

    }

    public Boolean checkvalidation()
    {
        EditText Email = (EditText)findViewById(R.id.txtprofilemail);
        EditText Password = (EditText)findViewById(R.id.txtprofilpassword);

        if( Email.getText().length() == 0 )
        {
            Email.setError( "APIEmail is required!" );
            return false;
        }
        else if (Password.getText().length() == 0)
        {
            Password.setError( "Password is required!" );
            return false;
        }
        else if( !(Email.getText().toString().matches("[a-zA-Z0-9._-]+@[a-z]+\\.+[a-z]+")))
        {
            Email.setError( "APIEmail is not Valid!" );
            return false;
        }
        else if( ( (Password.getText().length()) < 4 ) ||  ((Password.getText().length() > 32 )))
        {
            Password.setError( "Password should be between 4 to 32 characters!" );
            return false;
        }
        else
        {
            return true;
        }

    }
    public Boolean setsharedpreference(String email, String password)
    {

        try
        {

            SharedPreferences sharedPreferences = getSharedPreferences("logindata", Context.MODE_PRIVATE);
            SharedPreferences.Editor editor = sharedPreferences.edit();
            editor.putString("email",email);
            editor.putString("password",password);

            editor.apply();
            return true;
        }
        catch (Exception e)
        {
            return false;

        }





    }
}
