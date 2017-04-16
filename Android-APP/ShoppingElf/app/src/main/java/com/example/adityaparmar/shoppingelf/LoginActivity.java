package com.example.adityaparmar.shoppingelf;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

/**
 * A login screen that offers login via email/password.
 */
public class LoginActivity extends AppCompatActivity{

    EditText email;
    EditText password;
    Button signin;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        email = (EditText)findViewById(R.id.email);
        password = (EditText)findViewById(R.id.password);
        signin = (Button)findViewById(R.id.sigin);


    }

    public void savelogindata(View view)
    {
        SharedPreferences sharedPreferences = getSharedPreferences("userlogindata", Context.MODE_PRIVATE);
        SharedPreferences.Editor editor = sharedPreferences.edit();
        editor.putString("email",email.getText().toString());
        editor.putString("password",password.getText().toString());
        editor.apply();
        Toast.makeText(this,"Successfully Log In",Toast.LENGTH_LONG).show();
        Intent i = new Intent(this, Home.class);
        //i.putExtra("email",email);
        startActivity(i);
    }
}

