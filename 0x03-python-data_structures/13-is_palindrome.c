#include "lists.h"
#include <stdlib.h>

/**
 * reverse_list - Reverses a linked list.
 * @head_ref: Pointer to the pointer to the head of the list.
 * Return: Pointer to the new head of the reversed list.
 */
listint_t *reverse_list(listint_t **head_ref)
{
    listint_t *prev = NULL;
    listint_t *current = *head_ref;
    listint_t *next = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head_ref = prev;
    return prev;
}

/**
 * compare_lists - Compares two linked lists.
 * @head1: Pointer to the head of the first list.
 * @head2: Pointer to the head of the second list.
 * Return: 1 if lists are equal, else 0.
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

/**
 * is_palindrome - Checks if a linked list is a palindrome.
 * @head: Pointer to a pointer to the head of the list.
 * Return: 1 if it is a palindrome, else 0.
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow_ptr = *head;
    listint_t *fast_ptr = *head;
    listint_t *prev_slow_ptr = *head;
    listint_t *second_half = NULL;
    listint_t *mid_node = NULL;
    int is_pal = 1;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    // Find the middle of the list using the slow and fast pointers
    while (fast_ptr != NULL && fast_ptr->next != NULL)
    {
        fast_ptr = fast_ptr->next->next;
        prev_slow_ptr = slow_ptr;
        slow_ptr = slow_ptr->next;
    }

    // If the list has an odd number of elements, move the slow pointer to the next node
    if (fast_ptr != NULL)
    {
        mid_node = slow_ptr;
        slow_ptr = slow_ptr->next;
    }

    // Reverse the second half of the list
    second_half = reverse_list(&slow_ptr);

    // Compare the first and second halves of the list
    is_pal = compare_lists(*head, second_half);

    // Restore the original list by reversing the second half back and joining it with the first half
    if (mid_node != NULL)
    {
        prev_slow_ptr->next = mid_node;
        mid_node->next = second_half;
    }
    else
    {
        prev_slow_ptr->next = second_half;
    }

    return is_pal;
}
