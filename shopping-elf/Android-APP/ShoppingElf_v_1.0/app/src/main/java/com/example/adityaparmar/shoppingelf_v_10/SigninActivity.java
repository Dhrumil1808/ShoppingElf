package com.example.adityaparmar.shoppingelf_v_10;

import android.content.Context;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.example.adityaparmar.shoppingelf_v_10.model.MySignInRequest;
import com.example.adityaparmar.shoppingelf_v_10.model.MySignInResponse;
import com.example.adityaparmar.shoppingelf_v_10.service.SignInClient;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class SigninActivity extends AppCompatActivity {


    Button btnSignIn;
    EditText Email;
    EditText Password;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_signin);

        btnSignIn = (Button) findViewById(R.id.btnSignIn);

        Email = (EditText) findViewById(R.id.txtsigninemail);
        Password = (EditText) findViewById(R.id.txtsignpassword);


        btnSignIn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                //Toast.makeText(LoginActivity.this,Email.getText().toString()+Email.getText().length(),Toast.LENGTH_LONG).show();


                if (checkvalidation()) {


                 Checkserverlogindata(Email.getText().toString(),Password.getText().toString());


                }


            }
        });

    }

    public Boolean checkvalidation() {
        Email = (EditText) findViewById(R.id.txtsigninemail);
        Password = (EditText) findViewById(R.id.txtsignpassword);

        if (Email.getText().length() == 0) {
            Email.setError("Email is required!");
            return false;
        } else if (Password.getText().length() == 0) {
            Password.setError("Password is required!");
            return false;
        } else if (!(Email.getText().toString().matches("[a-zA-Z0-9._-]+@[a-z]+\\.+[a-z]+"))) {
            Email.setError("Email is not Valid!");
            return false;
        } else if (((Password.getText().length()) < 4) || ((Password.getText().length() > 32))) {
            Password.setError("Password should be between 4 to 32 characters!");
            return false;
        } else {
            return true;
        }

    }

    public Boolean Checkserverlogindata(final String email, final String password) {


        MySignInRequest mySignInRequest = new MySignInRequest();
        mySignInRequest.setEmail(email);
        mySignInRequest.setPassword(password);


        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl("http://54.241.140.236:3009")
                .addConverterFactory(GsonConverterFactory.create())
                .build();



        //SignUpClient signUpClient = retrofit.create(SignUpClient.class);

        SignInClient signInClient = retrofit.create(SignInClient.class);


        Call<MySignInResponse> callsignin = signInClient.checkuser(mySignInRequest);




        callsignin.enqueue(new Callback<MySignInResponse>() {
            @Override
            public void onResponse(Call<MySignInResponse> call, Response<MySignInResponse> response) {
                //Snackbar.make(findViewById(R.id.main_content), "Account created Successfully",Snackbar.LENGTH_LONG).show();

                Toast.makeText(SigninActivity.this,response.body().getMessage(),Toast.LENGTH_LONG).show();

               // setsharedpreference(email,password);
                //Intent i = new Intent(SigninActivity.this,MainActivity.class);
                //startActivity(i);


            }

            @Override
            public void onFailure(Call<MySignInResponse> call, Throwable t) {
                Snackbar.make(findViewById(R.id.rllogin), "Something went wrong !!",Snackbar.LENGTH_LONG).show();

            }
        });

        return false;

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
