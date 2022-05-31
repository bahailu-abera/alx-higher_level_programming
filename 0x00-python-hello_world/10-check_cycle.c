#include <stdlib.h>
#include "lists.h"
#include <stdio.h>


/**
 * check_cycle - checks if their is a loop in a linked list
 * @list: pointer to  linked list structure
 *
 *Return: 0 if there is no cycle, 1 if there is a cycle
 *
 */
int check_cycle(listint_t *list)
{
	/*listint_t *slow, *fast;

	if (list == NULL)
		return (0);

	slow = list;
	fast = list;

	if (fast->next)
		fast = fast->next;

	while (fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (fast == slow)
			return (1);
	}*/
	listint_t *temp;
	listint_t *prev;
	temp = malloc(sizeof(listint_t));
	if (temp == NULL)
		return (0);
	temp->n = 4;
	temp->next = NULL;
	
	while (list != NULL)
	{
		prev = list;
		list = list->next;
		prev->next = temp;

		if (list == temp)
			return (1);
	}
	free(temp);

	return (0);
}

