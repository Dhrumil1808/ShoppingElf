package com.example.adityaparmar.shoppingelf;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);






        Boolean res = getloginuserdata();     //authonticationlogin(email,password);
        if(res)
        {
            Intent i = new Intent(this, Home.class);
            //i.putExtra("email",email);
            startActivity(i);
        }
        else {
            Intent j = new Intent(this, LoginActivity.class);
            startActivity(j);
        }

    }

    public Boolean authonticationlogin(String email, String password)
    {
        Boolean res = true;


        // write Rest API code
        // call Rest Api which will authorise user credentials and return boolean value



        return  res;
    }

    public Boolean getloginuserdata()
    {
        Boolean res = false;
        SharedPreferences sharedPreferences = getSharedPreferences("userlogindata", Context.MODE_PRIVATE);
        String email = sharedPreferences.getString("email","");
        String password = sharedPreferences.getString("password","");

        if(!email.isEmpty())
        {
           if(authonticationlogin(email,password)){

               res=true;
               Toast.makeText(this,email+"  "+password,Toast.LENGTH_LONG).show();
           }
            else
           {
               res=false;
           }

        }
        else
        {
            res=false;
        }



        return res;
    }
}


