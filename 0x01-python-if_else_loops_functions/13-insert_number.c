#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: head
 * @number: number to store in the new node
 * Return: pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
        listint_t *prev;
        listint_t *curr;

        prev = *head;

        curr = malloc(sizeof(listint_t));
        if (curr == NULL)
                return (NULL);
        curr->n = number;

        if (*head == NULL || (*head)->n > number)
        {
                curr->next = *head;
                *head = curr;
                return (curr);
        }

        while (prev->next != NULL)
        {
                if ((prev->next)->n >= number)
                {
                        curr->next = prev->next;
                        prev->next = curr;
                        return (curr);
                }
                prev = prev->next;
        }

        curr->next = NULL;
        prev->next = curr;
        return (curr);
}
