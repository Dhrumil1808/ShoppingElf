package com.example.adityaparmar.shoppingelf_v_10;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.example.adityaparmar.shoppingelf_v_10.model.MySignupRequest;
import com.example.adityaparmar.shoppingelf_v_10.model.MySignupResponse;
import com.example.adityaparmar.shoppingelf_v_10.service.SignUpClient;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class LoginActivity extends AppCompatActivity {



    Button btnCreateAccount;
    EditText Email;
    EditText Password;
    EditText Family_member;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);


        btnCreateAccount = (Button)findViewById(R.id.btnCreateAccount);
        Email = (EditText)findViewById(R.id.txtemail);
        Password = (EditText)findViewById(R.id.txtpassword);
        Family_member = (EditText) findViewById(R.id.txtfamilymembers);






        btnCreateAccount.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                if(checkvalidation()) {

                   Boolean res = createaccount(Email.getText().toString(),Password.getText().toString(),Family_member.getText().toString());
                    Toast.makeText(LoginActivity.this,res.toString(),Toast.LENGTH_LONG);
                }
                else
                {

                }



            }
        });



    }

    public Boolean createaccount(final String email, final String password, final String familymember)
    {


        MySignupRequest mySignupRequest = new MySignupRequest();
        mySignupRequest.setEmail(email);
        mySignupRequest.setPassword(password);
        mySignupRequest.setFamily_member(Integer.parseInt(familymember));

        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl("http://54.241.140.236:3009")
                .addConverterFactory(GsonConverterFactory.create())
                .build();



        SignUpClient signUpClient = retrofit.create(SignUpClient.class);

        Call<MySignupResponse> callsignup = signUpClient.createUser(mySignupRequest);




        callsignup.enqueue(new Callback<MySignupResponse>() {
            @Override
            public void onResponse(Call<MySignupResponse> call, Response<MySignupResponse> response) {
                //Snackbar.make(findViewById(R.id.main_content), "Account created Successfully",Snackbar.LENGTH_LONG).show();
                //setsharedpreference(email,password,familymember);
                Intent i = new Intent(LoginActivity.this,SigninActivity.class);
                startActivity(i);

            }

            @Override
            public void onFailure(Call<MySignupResponse> call, Throwable t) {
                Snackbar.make(findViewById(R.id.rllogin), "Something went wrong !!",Snackbar.LENGTH_LONG).show();

            }
        });

        return false;
    }



    public Boolean setsharedpreference(String email, String password,String family_members)
    {

        try
        {

            SharedPreferences sharedPreferences = getSharedPreferences("logindata", Context.MODE_PRIVATE);
            SharedPreferences.Editor editor = sharedPreferences.edit();
            editor.putString("email",email);
            editor.putString("password",password);
            editor.putString("family_members",family_members);
            editor.apply();
            return true;
        }
        catch (Exception e)
        {
            return false;

        }





    }


    public Boolean checkvalidation()
    {
        Email = (EditText)findViewById(R.id.txtemail);
        Password = (EditText)findViewById(R.id.txtpassword);

        if( Email.getText().length() == 0 )
        {
            Email.setError( "Email is required!" );
            return false;
        }
        else if (Password.getText().length() == 0)
        {
            Password.setError( "Password is required!" );
            return false;
        }
        else if( !(Email.getText().toString().matches("[a-zA-Z0-9._-]+@[a-z]+\\.+[a-z]+")))
        {
            Email.setError( "Email is not Valid!" );
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

}
