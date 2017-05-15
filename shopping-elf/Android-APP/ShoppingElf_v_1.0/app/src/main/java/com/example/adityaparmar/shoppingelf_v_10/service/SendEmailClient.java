package com.example.adityaparmar.shoppingelf_v_10.service;

import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.http.GET;
import retrofit2.http.Path;

/**
 * Created by adityaparmar on 5/14/17.
 */

public interface SendEmailClient {

    @GET("/inventory/mail/{useremailid}")
    Call<ResponseBody> sendmail(@Path("useremailid") String useremailid);
}
