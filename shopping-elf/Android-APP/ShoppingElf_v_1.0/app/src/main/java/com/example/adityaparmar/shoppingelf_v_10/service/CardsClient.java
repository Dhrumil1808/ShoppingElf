package com.example.adityaparmar.shoppingelf_v_10.service;

import com.example.adityaparmar.shoppingelf_v_10.model.MyCards;

import java.util.List;

import retrofit2.Call;
import retrofit2.http.GET;

/**
 * Created by adityaparmar on 5/8/17.
 */

public interface CardsClient {

    @GET("/inventory/list/aditya")
    Call<List<MyCards>> getcards();
}
