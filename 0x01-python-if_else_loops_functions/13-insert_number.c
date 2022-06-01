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
	listint_t *cur, *prev;

	if (head == NULL)
		return (NULL);

	prev = NULL;
	for (cur = *head; cur->n < number && cur != NULL;
	     prev = cur, cur = cur->next)
		;

	cur = malloc(sizeof(listint_t));
	cur->n = number;

	if (prev == NULL)
	{
		cur->next = NULL;
		*head = cur;

		return (cur);
	}

	cur->next = prev->next;
	prev->next = cur;
	return (cur);
}
