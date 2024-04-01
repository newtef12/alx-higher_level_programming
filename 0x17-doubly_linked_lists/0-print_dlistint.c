#include "lists.h"
#include <stdio.h>

/**
 * print_dlistint - prints all the elements of a dlistint_t list
 * @h: head of the list
 *
 * Return: the number of nodes
 */
size_t print_dlistint(const dlistint_t *h)
{
    size_t count = 0; // Variable to keep track of the number of nodes

    // Loop to iterate through the list and print each element
    while (h != NULL)
    {
        printf("%d\n", h->n); // Print the value of the current node
        count++; // Increment the count of nodes
        h = h->next; // Move to the next node
    }

    return (count); // Return the total count of nodes
}
