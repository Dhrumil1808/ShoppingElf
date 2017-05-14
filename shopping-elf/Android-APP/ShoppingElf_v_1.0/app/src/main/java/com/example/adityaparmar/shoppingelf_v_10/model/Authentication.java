package com.example.adityaparmar.shoppingelf_v_10.model;

import android.content.Context;
import android.content.SharedPreferences;
import android.support.v7.app.AppCompatActivity;

/**
 * Created by adityaparmar on 5/11/17.
 */

public class Authentication extends AppCompatActivity {

    private String email;
    private String password;

    public Authentication() {
        this.email = email;
        this.password = password;
    }
    public Authentication(String email, String password) {
        this.email = email;
        this.password = password;
    }






    public String getsharedpreferenceemail(){


            SharedPreferences sharedPreferences = getSharedPreferences("userlogindata", Context.MODE_PRIVATE);
            String email = sharedPreferences.getString("email","");
            String password = sharedPreferences.getString("password","");


             return email;

    }



}
