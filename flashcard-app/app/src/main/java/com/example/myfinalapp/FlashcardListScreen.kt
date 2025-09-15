package com.example.myfinalapp

import androidx.compose.foundation.layout.*
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Delete
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.navigation.NavController
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items

@Composable
fun FlashcardListScreen(navController: NavController) {
    val flashcards = remember {
        mutableStateListOf<Flashcard>().apply {
            addAll(FlashcardDataSource.getAll())
        }
    }

    Column(modifier = Modifier
        .fillMaxSize()
        .padding(16.dp)) {

        Text("Flashcards", style = MaterialTheme.typography.headlineMedium)

        Spacer(modifier = Modifier.height(16.dp))

        LazyColumn(modifier = Modifier.weight(1f)) {
            items(flashcards) { card ->
                Card(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(vertical = 8.dp),
                    colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.surfaceVariant)
                ) {
                    Column(modifier = Modifier.padding(16.dp)) {
                        Text("Q: ${card.question}", style = MaterialTheme.typography.bodyLarge)
                        Spacer(modifier = Modifier.height(8.dp))
                        Text("A: ${card.answer}", style = MaterialTheme.typography.bodyMedium)
                        IconButton(onClick = {
                            FlashcardDataSource.delete(card)   // Remove from data source
                            flashcards.remove(card)            // Remove from UI list
                        }) {
                            Icon(Icons.Default.Delete, contentDescription = "Delete")
                        }

                    }
                }
            }
        }

        Spacer(modifier = Modifier.height(24.dp))

        Button(
            onClick = { navController.navigate("add") },
            modifier = Modifier.fillMaxWidth()
        ) {
            Text("Add New Flashcard")
        }
    }
}
