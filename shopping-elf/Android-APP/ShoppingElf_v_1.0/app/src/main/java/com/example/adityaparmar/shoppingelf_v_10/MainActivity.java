package com.example.adityaparmar.shoppingelf_v_10;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.support.design.widget.TabLayout;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentManager;
import android.support.v4.app.FragmentPagerAdapter;
import android.support.v4.view.ViewPager;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;

import com.example.adityaparmar.shoppingelf_v_10.service.SendEmailClient;

import okhttp3.OkHttpClient;
import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class MainActivity extends AppCompatActivity {

    /**
     * The {@link android.support.v4.view.PagerAdapter} that will provide
     * fragments for each of the sections. We use a
     * {@link FragmentPagerAdapter} derivative, which will keep every
     * loaded fragment in memory. If this becomes too memory intensive, it
     * may be best to switch to a
     * {@link android.support.v4.app.FragmentStatePagerAdapter}.
     */
    private SectionsPagerAdapter mSectionsPagerAdapter;

    /**
     * The {@link ViewPager} that will host the section contents.
     */
    private ViewPager mViewPager;

    private Boolean Islogged;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);
        // Create the com.example.adityaparmar.shoppingelf_v_10.adapter that will return a fragment for each of the three
        // primary sections of the activity.
        mSectionsPagerAdapter = new SectionsPagerAdapter(getSupportFragmentManager());

        // Set up the ViewPager with the sections com.example.adityaparmar.shoppingelf_v_10.adapter.
        mViewPager = (ViewPager) findViewById(R.id.container);
        mViewPager.setAdapter(mSectionsPagerAdapter);

        TabLayout tabLayout = (TabLayout) findViewById(R.id.tabs);

        tabLayout.setupWithViewPager(mViewPager);
        tabLayout.getTabAt(0).setIcon(R.drawable.cameraicon);
        tabLayout.getTabAt(1).setIcon(R.drawable.shoppingcarticon);
        tabLayout.getTabAt(2).setIcon(R.drawable.emailicon);


        // Bucket coding here

        Islogged = getsharedpreference();




    }



    public void Opencamera(View view)
    {

        if(Islogged)
        {
            Intent i = new Intent(this,UploadReceiptActivity.class);
            startActivity(i);
        }
        else
        {
            Intent i = new Intent(this,LoginActivity.class);
            startActivity(i);

        }


    }
    public void sendemail(View view){


        String sendingemail = getsharedpreferenceemail();

        String API_BASE_URL = "http://54.241.140.236:3008/";

        OkHttpClient.Builder httpClient = new OkHttpClient.Builder();

        Retrofit.Builder builder = new Retrofit.Builder()
                .baseUrl(API_BASE_URL)
                .addConverterFactory(
                        GsonConverterFactory.create()
                );

        Retrofit retrofit = builder.client(httpClient.build()).build();



        SendEmailClient sendEmailClient = retrofit.create(SendEmailClient.class);


        // Fetch a list of the Github repositories.

        if(sendingemail !="error")
        {
            Call<ResponseBody> call = sendEmailClient.sendmail(getsharedpreferenceemail());

            // Execute the call asynchronously. Get a positive or negative callback.
            call.enqueue(new Callback<ResponseBody>() {
                @Override
                public void onResponse(Call<ResponseBody> call, Response<ResponseBody> response) {


                }

                @Override
                public void onFailure(Call<ResponseBody> call, Throwable t) {

                }
            });

        }




    }
    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.

        if(Islogged)
        {
            getMenuInflater().inflate(R.menu.menu_main, menu);
            return true;
        }
        else
        {
            getMenuInflater().inflate(R.menu.menu_init, menu);
            return true;
        }

    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement

        if(id == R.id.action_signup) {

            Intent i = new Intent(this,LoginActivity.class);
            startActivity(i);

        }

        if(id == R.id.action_signin) {

            Intent i = new Intent(this,SigninActivity.class);
            startActivity(i);

        }

        if(id == R.id.action_forgot_password){

        }


        if(id == R.id.action_profile) {

            Intent i = new Intent(this,ProfileActivity.class);
            startActivity(i);
        }

        if(id == R.id.action_logout){

            Islogged = false;
            SharedPreferences sharedPreferences = getSharedPreferences("logindata", Context.MODE_PRIVATE);
            SharedPreferences.Editor editor = sharedPreferences.edit();
            editor.clear();
            editor.commit();
            Intent i = new Intent(this,MainActivity.class);
            startActivity(i);
        }


        return super.onOptionsItemSelected(item);
    }


    public class SectionsPagerAdapter extends FragmentPagerAdapter {

        public SectionsPagerAdapter(FragmentManager fm) {
            super(fm);
        }

        @Override
        public Fragment getItem(int position) {
            // getItem is called to instantiate the fragment for the given page.
            // Return a PlaceholderFragment (defined as a static inner class below).
            return PlaceholderFragment.newInstance(position + 1);
        }

        @Override
        public int getCount() {
            // Show 3 total pages.
            return 3;
        }


    }

    public Boolean getsharedpreference(){

        try
        {
            SharedPreferences sharedPreferences = getSharedPreferences("logindata", Context.MODE_PRIVATE);
            String email = sharedPreferences.getString("email","");
            String password = sharedPreferences.getString("password","");
            if(!email.isEmpty()) {
                return true;
            }
            else {
                return false;
            }
        }
        catch(Exception e)
        {
            return false;
        }

    }
    public String getsharedpreferenceemail(){

        try
        {
            SharedPreferences sharedPreferences = getSharedPreferences("logindata", Context.MODE_PRIVATE);
            String email = sharedPreferences.getString("email","");

            if(!email.isEmpty()) {
                return email;
            }
            else {
                return "error";
            }
        }
        catch(Exception e)
        {
            return "error";
        }

    }




}
/*

    References: http://stackoverflow.com/questions/34579614/how-to-implement-recyclerview-with-cardview-rows-in-a-fragment-with-tablayout

 */