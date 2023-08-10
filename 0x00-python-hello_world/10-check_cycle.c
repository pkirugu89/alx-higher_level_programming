#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - check cycle method
 * @list: list
 * Return: list 1 if cycle is found. Otherwise 0 if no cycle found
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			/* Cycle found */
			return (1);
	}
	/* No cycle found */
	return (0);
}
