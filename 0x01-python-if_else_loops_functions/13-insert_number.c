#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts node in a sorted linked list
 * @head: pointer to the linked list data structure head
 *@number: the value of the new node to be inserted
 *
 *Return: the address of the new node(success)
 * NULL (failure)
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *cur, *prev, *new;

	if (head == NULL)
		return (NULL);

	prev = NULL;
	for (cur = *head; cur->n < number && cur != NULL;
	     prev = cur, cur = cur->next)
		;

	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	new->n = number;

	if (prev == NULL)
	{
		new->next = NULL;
		*head = new;

		return (new);
	}

	new->next = prev->next;
	prev->next = new;
	return (new);
}
