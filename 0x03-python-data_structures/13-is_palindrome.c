#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer to the head of the list
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    if (*head == NULL || (*head)->next == NULL)
        return (1);

    listint_t *slow = *head, *fast = *head;
    listint_t *prev_slow = NULL, *second_half = NULL;
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
    is_palindrome = compare_lists(*head, second_half);

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

/**
 * reverse_list - reverses a linked list
 * @head_ref: pointer to pointer to the head of the list
 */
void reverse_list(listint_t **head_ref)
{
    listint_t *prev = NULL, *current = *head_ref, *next = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head_ref = prev;
}

/**
 * compare_lists - compares two linked lists
 * @head1: pointer to the head of the first list
 * @head2: pointer to the head of the second list
 * Return: 1 if lists are equal, 0 otherwise
 */
int compare_lists(listint_t *head1, listint_t *head2)
{
    while (head1 != NULL && head2 != NULL)
    {
        if (head1->n != head2->n)
            return 0;
        head1 = head1->next;
        head2 = head2->next;
    }

    // If both lists are NULL at this point, they are equal
    return (head1 == NULL && head2 == NULL);
}
