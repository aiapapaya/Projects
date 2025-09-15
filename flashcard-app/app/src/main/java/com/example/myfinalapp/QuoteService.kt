package com.example.myfinalapp

import retrofit2.http.GET

//  Data class to hold the response from the API
data class QuoteResponse(
    val content: String  // This holds the actual quote text
)

//  Retrofit interface to define the API endpoint
interface QuoteService {
    //  Tells Retrofit to make a GET request to the "random" endpoint
    @GET("random")
    suspend fun getRandomQuote(): QuoteResponse
}
