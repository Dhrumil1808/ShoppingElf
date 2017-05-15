package com.example.adityaparmar.shoppingelf_v_10.service;

import com.example.adityaparmar.shoppingelf_v_10.model.MyCards;

import java.util.List;

import retrofit2.Call;
import retrofit2.http.GET;
import retrofit2.http.Path;

/**
 * Created by adityaparmar on 5/8/17.
 */

public interface CardsClient {

    @GET("/inventory/list/{useremailid}")
    Call<List<MyCards>> getcards(@Path("useremailid") String useremailid);
}
