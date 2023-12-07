#include "lists.h"

/**
*add_nodeint - adds a new node at the beginning of the list
*@head: head of listint_t
*@n: int to add to the list
*Return: address of the new element
*/

listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = *head;
	*head = new;
	return (new);
}

/**
*is_palindrome - identify if a single linked list is a palindrome
*@head: head of listint_t
*Return: 1 if it is palindrome or 0 if not
*/

int is_palindrome(listint_t **head)
{
	listint_t *head_ptr = NULL;

	head_ptr = *head;
	listint_t *ptr1 = NULL, *ptr2 = NULL;

	if (*head == NULL || head_ptr->next == NULL)
		return (1);
	while (head_ptr != NULL)
	{
		add_nodeint(&ptr1, head_ptr->n);
		head_ptr = head_ptr->next;
	}
	ptr2 = ptr1;
	while (*head != NULL)
	{
		if ((*head)->n != ptr2->n)
		{
			free_listint(ptr1);
			return (0);
		}
		*head = (*head)->next;
		ptr2 = ptr2->next;
	}
	free_listint(ptr2);
	return (1);
}
