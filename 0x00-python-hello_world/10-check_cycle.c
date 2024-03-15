#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it.
 * @list: Pointer to the head of the linked list.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
    listint_t *slow = list;
    listint_t *fast = list;

    while (slow && fast && fast->next)
    {
        slow = slow->next;          /* Move slow pointer by one step */
        fast = fast->next->next;    /* Move fast pointer by two steps */

        if (slow == fast)           /* If slow and fast pointers meet, there's a cycle */
            return (1);
    }

    return (0);  /* No cycle found */
}
