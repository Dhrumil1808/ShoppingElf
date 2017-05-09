package com.example.adityaparmar.shoppingelf_v_10;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.widget.ListView;
import android.widget.Toast;

import com.example.adityaparmar.shoppingelf_v_10.model.GitHubRepo;
import com.example.adityaparmar.shoppingelf_v_10.service.GitHubClient;

import java.util.List;

import com.example.adityaparmar.shoppingelf_v_10.adapter.GitHubRepoAdapter;
import okhttp3.OkHttpClient;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;


public class Recto extends AppCompatActivity {

    private ListView listView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_recto);

       listView = (ListView) findViewById(R.id.listgithub);
        String API_BASE_URL = "https://api.github.com/";

        OkHttpClient.Builder httpClient = new OkHttpClient.Builder();

        Retrofit.Builder builder = new Retrofit.Builder()
                        .baseUrl(API_BASE_URL)
                        .addConverterFactory(
                                GsonConverterFactory.create()
                        );

        Retrofit retrofit = builder.client(httpClient.build()).build();



        GitHubClient client =  retrofit.create(GitHubClient.class);

        // Fetch a list of the Github repositories.
        Call<List<GitHubRepo>> call =
                client.reposForUser("fs-opensource");

        // Execute the call asynchronously. Get a positive or negative callback.
        call.enqueue(new Callback<List<GitHubRepo>>() {
            @Override
            public void onResponse(Call<List<GitHubRepo>> call, Response<List<GitHubRepo>> response) {
                // The network call was a success and we got a response
                // TODO: use the repository list and display it
                List<GitHubRepo> respo = response.body();
                listView.setAdapter(new GitHubRepoAdapter(Recto.this,respo));
                Toast.makeText(Recto.this,"positive responce",Toast.LENGTH_LONG);
            }

            @Override
            public void onFailure(Call<List<GitHubRepo>> call, Throwable t) {
                // the network call was a failure
                // TODO: handle error
            }
        });
    }
}
