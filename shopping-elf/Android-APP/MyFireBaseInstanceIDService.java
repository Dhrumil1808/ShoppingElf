package com.shopping.dhrumil.shopping;

import android.net.Uri;
import android.util.Log;

import com.google.firebase.iid.FirebaseInstanceId;
import com.google.firebase.iid.FirebaseInstanceIdService;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedWriter;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLConnection;
import java.net.URLEncoder;

/**
 * Created by dhrumil on 5/13/17.
 */

public class MyFireBaseInstanceIDService extends FirebaseInstanceIdService {
    private static final String TAG = "MyFirebaseIIDService";

    /**
     * Called if InstanceID token is updated. This may occur if the security of
     * the previous token had been compromised. Note that this is called when the InstanceID token
     * is initially generated so this is where you would retrieve the token.
     */
    // [START refresh_token]
    @Override
    public void onTokenRefresh() {
        // Get updated InstanceID token.
        String refreshedToken = FirebaseInstanceId.getInstance().getToken();
        Log.d(TAG, "Refreshed token: " + refreshedToken);

        // If you want to send messages to this application instance or
        // manage this apps subscriptions on the server side, send the
        // Instance ID token to your app server.
        sendRegistrationToServer(refreshedToken);
    }
    // [END refresh_token]

    /**
     * Persist token to third-party servers.
     * <p>
     * Modify this method to associate the user's FCM InstanceID token with any server-side account
     * maintained by your application.
     *
     * @param token The new token.
     */
    private void sendRegistrationToServer(String token) {

        // TODO: Implement this method to send token to your app server.
        Thread thread = new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    URL url = new URL("http://0.0.0.0:3009/user/update-api-key");

                    URLConnection urlConn=new URLConnection(url) {
                        @Override
                        public void connect() throws IOException {

                        }
                    };
                    DataOutputStream printout;
                    DataInputStream input;
                    HttpURLConnection conn = (HttpURLConnection) url.openConnection();
                    conn.setReadTimeout(10000);
                    conn.setConnectTimeout(15000);
                    conn.setRequestMethod("POST");
                    conn.setDoInput(true);
                    conn.setDoOutput(true);
                    conn.setRequestProperty("Content-Type","application/json");
                    conn.setRequestProperty("Host", "http://0.0.0.0:3009/user/update-api-key");
                    JSONObject jsonParam = new JSONObject();
                    try {
                        jsonParam.put("email", "rashmishrm74@gmail.com");
                        jsonParam.put("api-key", "fEsARrbxuDk:APA91bFc86uY-6SPIQxwgHFZVNVpi0CsKoxipTuXNLOkY2ubSr-i0WvbT6-8x0DenREXKI9hAO9koidqZAWRk8ImVOSviCG8QvaPTqXFxiQVeWHLyEc8bDUU2pWKZe2wwFBZpHjGZHvs");
                    }
                    catch(JSONException e)
                    {
                        e.printStackTrace();
                    }
                    Log.d("URL","URL:" + URLEncoder.encode(jsonParam.toString()));

                    printout = new DataOutputStream(urlConn.getOutputStream());
                    printout.writeBytes(URLEncoder.encode(jsonParam.toString(),"UTF-8"));
                    printout.flush ();
                    printout.close ();


// read the response

                }
                catch(IOException e)
                {
                    e.printStackTrace();
                }
            }
        });

        thread.start();

    }

}