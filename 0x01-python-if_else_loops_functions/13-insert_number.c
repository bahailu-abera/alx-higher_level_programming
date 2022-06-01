#include "main.h"

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

	if (head == NULL || *head == NULL)
		return (NULL);

	for (cur = *head; cur->value < number && cur != NULL; \
	     prev = cur, cur = cur->next)
		;

	if (cur == NULL)
		return (NULL);

	cur = malloc(sizeof(listint_t));
	cur->value = number;
	cur->next = prev->next;
	prev->next = cur;

	return (cur);
}
