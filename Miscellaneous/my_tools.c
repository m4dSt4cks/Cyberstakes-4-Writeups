#include "mytools.h"
#include <string.h>


//Make a new tool with the specified name and durability
struct tool* fabricateTool(char* tname, uint32_t tdur){
    if (!tname) {
        return NULL;
    }
    struct tool* t = (struct tool*) malloc(sizeof(struct tool));
    if (!t) {
        return NULL;
    }
    memset(t, 0, sizeof(struct tool));


    size_t length = 0;
    strncpy(t->name, tname, NAMESIZE);
    length = strnlen(tname, NAMESIZE - 1);
    t->name[length] = '\0';

    t->durability = (uint8_t)tdur;
    return t;
}


//Given a set of tools, generate a toolbox with a name and a message
struct toolbox* assembleToolbox(char* name, char* message, struct tool** tools, ssize_t count){
    if (!name || !message || !tools) {
        return NULL;
    }

    struct toolbox* tb = (struct toolbox* ) malloc(sizeof(struct toolbox));
    if (!tb) {
        return NULL;
    }
    memset(tb, 0, sizeof(struct toolbox));

    
    strncpy(tb->name, name, NAMESIZE);
    tb->name[NAMESIZE - 1] = '\0';
    
    strncpy(tb->message, message, MSIZE);
    tb->message[MSIZE - 1] = '\0';

    if (count <= 0){
        tb->toolbelt = NULL;
        return tb;
    }

    size_t acount = 0;
    for (size_t i = 0; i < count; i++){
	if(tools[i]){
            acount = i + 1;
        } else {
            break;
        }
    }
    

    struct tool** belt = malloc(sizeof(struct tool*) * (acount + 1));
    if (!belt) {
        memset(tb, 0, sizeof(struct toolbox));
        free(tb);
        return NULL;
    }
    memset(belt, 0, sizeof(struct tool*) * (acount + 1));

    for (size_t i = 0; i < acount; i++){
	belt[i] = (tools[i]);
    }
    belt[acount] = NULL; 

    tb->toolbelt = belt;
    return tb;
}

//Count the number of tools in the toolbox, and also read their descriptions and durabilities
int checkToolbox(struct toolbox* box){
    if (!box) {
        return 0;
    }
    if (box->toolbelt == NULL) return 0;
    printf("Box %s says: %s\n", box->name, box->message);


    struct tool* curTool = box->toolbelt[0];
    int count = 0;
    while (curTool != NULL && count < 0x7fffffff){
	if (curTool->name) {
        	printf("\tTool %d: %s\n", count + 1, curTool->name);
	} else {
        	printf("\tTool %d: \n", count + 1);
	}

        count++;
        curTool = box->toolbelt[count];
    }
    return count;
}

//Add a message to a toolbox
void addMessage(struct toolbox* tb, char* message){
    if (!tb || !message) {
        return;
    }
    memset(tb->message, 0, MSIZE);
    strncpy(tb->message, message, MSIZE);
    tb->message[MSIZE - 1] = '\0';
}

//Make a set of tools from a list of names and durabilities, and then turn that into a toolbox
struct toolbox* fillNewToolbox(char* name, char* message, char** names, uint32_t* durs, ssize_t count){
    if (!name || !message || !names || !durs) {
        return NULL;
    }
    if(count <= 0){
        return NULL;
    }

    struct tool** tools = malloc(sizeof(struct tool*) * count);
    if (!tools) {
        return NULL;
    }
    memset(tools, 0, sizeof(struct tool*) * count);

    struct tool* temp;
    for (ssize_t i = 0; i < count; i++) {
        temp = fabricateTool(names[i], durs[i]);
        if(temp) {
            tools[i] = temp;
        } else {
            for (ssize_t j = 0; j < i; j++) {
                memset(tools[j], 0, sizeof(struct tool));
                free(tools[j]);
            }
            memset(tools, 0, sizeof(struct tool*) * count);
            free(tools);
            return NULL;
        }
    }

    struct toolbox* result = assembleToolbox(name, message, tools, count);
    if (!result) {
        for (ssize_t j = 0; j < count; j++) {
            memset(tools[j], 0, sizeof(struct tool));
            free(tools[j]);
        }
        memset(tools, 0, sizeof(struct tool*) * count);
        free(tools);
    }

    return result;
}

int helperfunc(char* message){
    if (message) {
    	printf("%s\n", message);
	return 0;
    } else {
        return -1;
    }
}

//Assign a fastener to a tool, and specify what it does when it's used
void assignTool(struct tool* t, struct fastener* f, char* message){
    if (!t || !f || !message) {
        return;
    }

    int (*funcptr)(char*) = NULL;
    funcptr = &helperfunc;

    struct use* us = malloc(sizeof(struct use));
    if (!us) {
        return;
    }
    memset(us, 0, sizeof(struct use));

    size_t length = 0;
    strncpy(us->message, message, MSIZE);
    length = strnlen(message, MSIZE - 1);
    us->message[length] = '\0';
    while (length < MSIZE) {
        us->message[length] = '\0';
        length++;
    }
    us->func = funcptr;

    // should we check if this already exists? I'm afraid to double-free anything
    if (t->use_struct) {
        free(t->use_struct);
    }
    t->use_struct = us;
    t->target = f;
};


//Use the tool, using the use_struct field in the tool to know what to do, return -1 if something goes wrong
struct tool* useTool(struct tool* t){
    if (!t || !(t->target)) {
        return (struct tool*)-1;
    }

    if (((uint16_t)(t->durability) > (t->target->tightness)) && (t->target->tightness != 0)){
        printf("running: ");
        t->target->tightness = 0;
        if ((t->use_struct) && (t->use_struct->func) && (t->use_struct->message)) {
            t->use_struct->func(t->use_struct->message);
        } else { 
            return (struct tool*)-1;
        }
        t->target = NULL;
        return t;
    }

    if ((uint16_t)(t->durability) < (t->target->tightness)){
        t->target->tightness -= (uint16_t)(t->durability);
        if ((t->name) && (t->target->name)) {
            printf("%s isn't strong enough to tighten %s %d:%d\n", t->name, t->target->name, t->durability, t->target->tightness);
        } else { 
            return (struct tool*)-1;
        }
        t->durability = 0;
        return t;
    }

    // should we have an == case?
    return (struct tool*)-1;

}
