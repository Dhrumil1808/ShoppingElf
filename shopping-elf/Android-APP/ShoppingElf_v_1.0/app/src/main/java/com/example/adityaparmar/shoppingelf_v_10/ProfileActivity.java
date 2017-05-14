package com.example.adityaparmar.shoppingelf_v_10;

import android.content.Context;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.widget.EditText;

public class ProfileActivity extends AppCompatActivity {

    EditText txtemail;
    EditText txtpassword;
    EditText txt;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_profile);


        txtemail = (EditText)findViewById(R.id.txtprofilemail);
        txtpassword=(EditText)findViewById(R.id.txtprofilpassword);

        SharedPreferences sharedPreferences = getSharedPreferences("logindata", Context.MODE_PRIVATE);
        String email = sharedPreferences.getString("email","");
        String password = sharedPreferences.getString("password","");

        txtemail.setText(email);
        txtpassword.setText(password);


    }
}
