package com.example.adityaparmar.shoppingelf_v_10.service;

import com.example.adityaparmar.shoppingelf_v_10.model.MySignupResponse;
import com.example.adityaparmar.shoppingelf_v_10.model.MySignupRequest;

import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.POST;

/**
 * Created by adityaparmar on 5/13/17.
 */

public interface SignUpClient {

   @POST("/user/signup")
   Call<MySignupResponse> createUser(@Body MySignupRequest mySignupRequest);


}
