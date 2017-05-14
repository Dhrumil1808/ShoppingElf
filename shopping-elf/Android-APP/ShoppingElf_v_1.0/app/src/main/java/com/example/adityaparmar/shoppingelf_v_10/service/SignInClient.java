package com.example.adityaparmar.shoppingelf_v_10.service;

import com.example.adityaparmar.shoppingelf_v_10.model.MySignInRequest;
import com.example.adityaparmar.shoppingelf_v_10.model.MySignInResponse;

import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.POST;

/**
 * Created by adityaparmar on 5/14/17.
 */

public interface SignInClient {
    @POST("/user/authenticate")
    Call<MySignInResponse> checkuser(@Body MySignInRequest mySignInRequest);
}
