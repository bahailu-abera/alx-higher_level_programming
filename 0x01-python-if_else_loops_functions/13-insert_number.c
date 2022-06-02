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


	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	cur = *head;

	for (prev = NULL; cur != NULL && cur->n < number;
	     prev = cur, cur = cur->next)
		;

	if (prev == NULL)
	{
		new->next = cur;
		*head = new;
		return (new);
	}

	new->next = prev->next;
	prev->next = new;

	return (new);
}
