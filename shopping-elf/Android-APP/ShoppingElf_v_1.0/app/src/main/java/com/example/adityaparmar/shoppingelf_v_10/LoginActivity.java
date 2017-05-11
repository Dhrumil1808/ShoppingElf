package com.example.adityaparmar.shoppingelf_v_10;

import android.content.DialogInterface;
import android.content.Intent;
import android.os.Bundle;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

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
            public void onClick(View v)
            {
                //Toast.makeText(LoginActivity.this,Email.getText().toString()+Email.getText().length(),Toast.LENGTH_LONG).show();


                if(checkvalidation())
                {

                    if(getAuth(Email.getText().toString(),Password.getText().toString()))
                    {
                        Snackbar.make(findViewById(R.id.rllogin), "Successfully Logged In.",Snackbar.LENGTH_LONG).show();

                    }
                    else
                    {
                        Snackbar.make(findViewById(R.id.rllogin), "Credentials are wrong, Try Again .",Snackbar.LENGTH_LONG).show();

                    }


                }


            }
        });

        btnCreateAccount.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                if(checkvalidation())
                {
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

                                            Boolean result = createaccount(Email.getText().toString(),Password.getText().toString(),userInput.getText().toString());
                                            if(result)
                                            {
                                                Snackbar.make(findViewById(R.id.rllogin), "Account created Successfully",Snackbar.LENGTH_LONG).show();

                                                Intent gotomainactivity = new Intent(LoginActivity.this,MainActivity.class);
                                                startActivity(gotomainactivity);
                                            }
                                            else
                                            {
                                                Snackbar.make(findViewById(R.id.rllogin), "Something went wrong, Try Again.",Snackbar.LENGTH_LONG).show();

                                            }

                                        }
                                    })
                            .setNegativeButton("Cancel",
                                    new DialogInterface.OnClickListener() {
                                        public void onClick(DialogInterface dialog,int id) {
                                            dialog.cancel();
                                            Snackbar.make(findViewById(R.id.rllogin), "Please Enter number of family members.",Snackbar.LENGTH_LONG).show();

                                        }
                                    });

                    // create alert dialog
                    AlertDialog alertDialog = alertDialogBuilder.create();

                    // show it
                    alertDialog.show();
                }



            }
        });



    }
    public Boolean getAuth(String email, String password)
    {


        return false;

    }
    public Boolean createaccount(String email, String password, String familymember)
    {
        return false;
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
