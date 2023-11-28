/*
 * File: 10-check_cycle.c
 * Auth: Brennan D Baraban
 */

#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if linked list contains a cycle.
 * @list: linked list.
 *
 * Return: If there is no cycle 0 else - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *curr, *prev;

	if (list == NULL || list->next == NULL)
		return (0);

	curr = list->next;
	prev = list->next->next;

	while (curr && prev && prev->next)
	{
		if (curr == prev)
			return (1);

		curr = curr->next;
		prev = prev->next->next;
	}

	return (0);
}
