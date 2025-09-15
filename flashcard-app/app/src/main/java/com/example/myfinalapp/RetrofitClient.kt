package com.example.myfinalapp

import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

object RetrofitClient {
    // 🌐 Lazy-initialized Retrofit instance to fetch fun facts (quotes) from an API
    val api: QuoteService by lazy {
        Retrofit.Builder()
            // ye Base URL of the public API that gives random quotes
            .baseUrl("http://api.quotable.io/")

            //  Use Gson to automatically convert JSON responses into Kotlin objects
            .addConverterFactory(GsonConverterFactory.create())

            //  Build the Retrofit instance and create the QuoteService interface
            .build()
            .create(QuoteService::class.java)
    }
}
