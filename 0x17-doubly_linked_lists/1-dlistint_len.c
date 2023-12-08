#include "lists.h"

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
