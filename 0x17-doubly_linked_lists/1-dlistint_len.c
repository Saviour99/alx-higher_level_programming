#include "lists.h"

/**
 *dlistint_len - return the number of elementin doubly linked list
 *@h: head of the list
 *
 *Return: number of element
 */

size_t dlistint_len(const dlistint_t *h)
{
	size_t elm = 0;

	while (h != NULL)
	{
		elm++;
		h = h->next;
	}
	return (elm);
}
