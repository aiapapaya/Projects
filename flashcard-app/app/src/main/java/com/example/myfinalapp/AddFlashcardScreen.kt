package com.example.myfinalapp

import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.navigation.NavController
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import com.example.myfinalapp.RetrofitClient

@Composable
fun AddFlashcardScreen(navController: NavController) {
    var question by remember { mutableStateOf("") }
    var answer by remember { mutableStateOf("") }
    var funFact by remember { mutableStateOf("Loading fun fact...") }

    //  Automatically fetch a fun fact when the screen loads
    LaunchedEffect(Unit) {
        try {
            println("📡 Trying to fetch quote...")
            val response = withContext(Dispatchers.IO) {
                RetrofitClient.api.getRandomQuote()
            }
            println("✅ Quote fetched: ${response.content}")
            funFact = response.content
        } catch (e: Exception) {
            println("❌ Error fetching quote: ${e.stackTraceToString()}")
            funFact = "Could not load fun fact.\nReason: ${e.message ?: "unknown error"}"
        }
    }

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(16.dp)
    ) {
        //  Screen heading
        Text("Add Flashcard", style = MaterialTheme.typography.headlineMedium)
        Spacer(modifier = Modifier.height(16.dp))

        //  User input field for the flashcard question
        OutlinedTextField(
            value = question,
            onValueChange = { question = it },
            label = { Text("Question") },
            modifier = Modifier.fillMaxWidth()
        )

        Spacer(modifier = Modifier.height(8.dp))

        //  User input field for the flashcard answer
        OutlinedTextField(
            value = answer,
            onValueChange = { answer = it },
            label = { Text("Answer") },
            modifier = Modifier.fillMaxWidth()
        )

        Spacer(modifier = Modifier.height(16.dp))

        //  Displaying the fun fact fetched from the API
        Text("Fact of the day: ", style = MaterialTheme.typography.bodyMedium)
        Text(funFact, style = MaterialTheme.typography.bodySmall)

        Spacer(modifier = Modifier.height(16.dp))

        //  Save button: adds flashcard only if both fields are filled
        Button(
            onClick = {
                if (question.isNotBlank() && answer.isNotBlank()) {
                    FlashcardDataSource.add(Flashcard(question, answer))
                    navController.popBackStack() // 🔙 Return to the list screen
                }
            },
            modifier = Modifier.fillMaxWidth()
        ) {
            Text("Save")
        }
    }
}
