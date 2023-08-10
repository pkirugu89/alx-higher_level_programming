#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	/* create a new node */
	listint_t *new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		return NULL;
	}
	new_node->n = number;
	new_node->next = NULL;
	/* check if the list is empty or if the new node should be the new head */
	if (*head == NULL || number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return new_node;
	}
	/* Traverse the list to find the appropriate position to insert the new node */
	current = *head;
	while (current->next != NULL && current->next->n <= number)
	{
		current = current->next;
	}
	/* Insert the new node after the current node */
	new_node->next = current->next;
	current->next = new_node;

	return new_node;
}
/* Helper function to print the linked list */
void print_list(listint_t *head)
{
	while (head != NULL)
	{
		printf("%d ", head->n);
		head = head->next;
	}
	printf("\n");
}
