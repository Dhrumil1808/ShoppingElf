package com.example.adityaparmar.shoppingelf_v_10.service;

import okhttp3.MultipartBody;
import okhttp3.RequestBody;
import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.http.Multipart;
import retrofit2.http.POST;
import retrofit2.http.Part;

/**
 * Created by adityaparmar on 5/9/17.
 */

public interface UploadImageClient {

    @Multipart
    @POST("/bill/upload/aditya")
    Call<ResponseBody> postImage(@Part MultipartBody.Part file, @Part("billDate") RequestBody billDate);
}
