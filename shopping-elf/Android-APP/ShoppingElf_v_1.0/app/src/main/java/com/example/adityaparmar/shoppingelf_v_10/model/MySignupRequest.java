package com.example.adityaparmar.shoppingelf_v_10.model;

/**
 * Created by adityaparmar on 5/13/17.
 */

public class MySignupRequest {
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

    public int getFamily_member() {
        return family_members;
    }

    public void setFamily_member(int family_member) {
        this.family_members = family_member;
    }

    private String email;
    private String password;
    private int family_members;




}
