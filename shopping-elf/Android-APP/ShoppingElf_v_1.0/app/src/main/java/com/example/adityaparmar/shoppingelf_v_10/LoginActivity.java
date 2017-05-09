package com.example.adityaparmar.shoppingelf_v_10;

import android.content.DialogInterface;
import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class LoginActivity extends AppCompatActivity {


    Button btnLogIn;
    Button btnCreateAccount;
    EditText Email;
    EditText Password;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        btnLogIn = (Button)findViewById(R.id.btnLogIn);
        btnCreateAccount = (Button)findViewById(R.id.btnCreateAccount);
        Email = (EditText)findViewById(R.id.txtemail);
        Password = (EditText)findViewById(R.id.txtpassword);




        btnLogIn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                if( Email.getText().toString().length() == 0 )
                {

                    Email.setError( "Email is required!" );
                }
                else if( Email.getText().toString().matches("[a-zA-Z0-9._-]+@[a-z]+\\.+[a-z]+"))
                {
                    Email.setError( "Email is not Valid!" );
                }
                else if(Password.getText().toString().length() == 0)
                {
                    Password.setError( "Password is required!" );
                }
                else if( ( (Password.getText().toString().length()) < 4 ) &&  ((Password.getText().toString().length() > 32 )))
                {
                    Password.setError( "Password should be between 4 to 32 characters" );
                }
                else
                {
                    Intent gotomainactivity = new Intent(LoginActivity.this,MainActivity.class);
                    startActivity(gotomainactivity);
                }


            }
        });

        btnCreateAccount.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                LayoutInflater li = LayoutInflater.from(LoginActivity.this);
                View promptsView = li.inflate(R.layout.promt_familymember, null);

                AlertDialog.Builder alertDialogBuilder = new AlertDialog.Builder(
                        LoginActivity.this);

                // set prompts.xml to alertdialog builder
                alertDialogBuilder.setView(promptsView);

                final EditText userInput = (EditText) promptsView
                        .findViewById(R.id.txtfamilymember);

                // set dialog message
                alertDialogBuilder
                        .setCancelable(false)
                        .setPositiveButton("OK",
                                new DialogInterface.OnClickListener() {
                                    public void onClick(DialogInterface dialog,int id) {
                                        // get user input and set it to result
                                        // edit text
                                        Toast.makeText(LoginActivity.this,userInput.getText().toString(),Toast.LENGTH_LONG).show();
                                        Intent gotomainactivity = new Intent(LoginActivity.this,MainActivity.class);
                                        startActivity(gotomainactivity);
                                    }
                                })
                        .setNegativeButton("Cancel",
                                new DialogInterface.OnClickListener() {
                                    public void onClick(DialogInterface dialog,int id) {
                                        dialog.cancel();
                                    }
                                });

                // create alert dialog
                AlertDialog alertDialog = alertDialogBuilder.create();

                // show it
                alertDialog.show();


            }
        });
    }


}
