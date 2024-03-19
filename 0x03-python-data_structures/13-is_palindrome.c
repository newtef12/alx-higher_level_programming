#include "lists.h"
#include <stdio.h>

/**
 * reverse_list - Reverses a linked list.
 * @head: Pointer to pointer to the head of the list.
 */
void reverse_list(listint_t **head)
{
    listint_t *prev = NULL;
    listint_t *current = *head;
    listint_t *next;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head = prev;
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to pointer to the head of the list.
 *
 * Return: 1 if palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
    if (*head == NULL || (*head)->next == NULL)
        return (1);

    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev_slow = NULL;
    listint_t *second_half = NULL;
    listint_t *mid_node = NULL;
    int is_palindrome = 1;

    // Find the middle of the list using slow and fast pointers
    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prev_slow = slow;
        slow = slow->next;
    }

    // If the list has odd number of elements, move slow pointer to the next node
    if (fast != NULL)
    {
        mid_node = slow;
        slow = slow->next;
    }

    // Reverse the second half of the list
    second_half = slow;
    prev_slow->next = NULL;
    reverse_list(&second_half);

    // Compare the first and second halves of the list
    while (*head != NULL && second_half != NULL)
    {
        if ((*head)->n != second_half->n)
        {
            is_palindrome = 0;
            break;
        }
        *head = (*head)->next;
        second_half = second_half->next;
    }

    // Restore the original list by reversing the second half back and joining it
    // with the first half
    if (mid_node != NULL)
    {
        prev_slow->next = mid_node;
        mid_node->next = second_half;
    }
    else
    {
        prev_slow->next = second_half;
    }

    return is_palindrome;
}
