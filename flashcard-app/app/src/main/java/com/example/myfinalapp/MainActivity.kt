package com.example.myfinalapp

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import com.example.myfinalapp.ui.theme.MyFinalAppTheme


class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            MyFinalAppTheme {
                Surface(color = MaterialTheme.colorScheme.background) {
                    val navController = rememberNavController()
                    //  NavHost defines the navigation graph
                    NavHost(navController, startDestination = "list") {
                        //  "list" screen shows the list of flashcards
                        composable("list") { FlashcardListScreen(navController) }
                        //  "add" screen lets user add a new flashcard
                        composable("add") { AddFlashcardScreen(navController) }
                    }
                }
            }
        }
    }
}
