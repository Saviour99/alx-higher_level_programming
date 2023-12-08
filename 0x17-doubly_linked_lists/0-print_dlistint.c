#include "lists.h"

/**
 *print_dlistint - print all element of the doubly linked list
 *@h: head of the list
 *
 * Return: addess of the head pointer
 */

size_t print_dlistint(const dlistint_t *h)
{
	int node = 0;
	const dlistint_t *temp = NULL;

	temp = malloc(sizeof(dlistint_t *));
	temp = h;
	while (temp != NULL)
	{
		node++;
		printf("%d\n", temp->n);
		temp = temp->next;
	}
	return (node);
}
