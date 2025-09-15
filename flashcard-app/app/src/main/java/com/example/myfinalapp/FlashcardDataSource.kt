// FlashcardDataSource.kt
package com.example.myfinalapp

object FlashcardDataSource {
    private val flashcards = mutableListOf<Flashcard>()

    fun getAll(): List<Flashcard> = flashcards

    fun add(card: Flashcard) {
        flashcards.add(card)
    }

    fun delete(card: Flashcard) {
        flashcards.remove(card)
    }

    fun clearAll() {
        flashcards.clear()
    }
}
