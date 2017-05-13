package com.shopping.dhrumil.shopping;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;


public class MainActivity extends AppCompatActivity {

    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        String SENDER_ID = "956003788897";
        Log.d("Id", "SENDER ID " + SENDER_ID);
        gettoken();
    }

    public void gettoken()
    {
        MyFireBaseInstanceIDService service=new MyFireBaseInstanceIDService();
        service.onTokenRefresh();
    }
}
