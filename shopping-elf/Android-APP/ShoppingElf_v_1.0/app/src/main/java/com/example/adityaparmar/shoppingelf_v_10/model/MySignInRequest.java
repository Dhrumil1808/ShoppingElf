package com.example.adityaparmar.shoppingelf_v_10.model;

/**
 * Created by adityaparmar on 5/14/17.
 */

public class MySignInRequest {


    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    private String email;
    private String password;
}
