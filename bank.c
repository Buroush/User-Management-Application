#include<stdio.h>
struct user
 {
 	char name[20];
 	int ac;
 	int pin;
 	int ab;
    int block;
};
void opening(struct user *ptr,int *p)
{
    int pi;
    ptr+=(*p);
    (*ptr).block=1;
    printf("Plese Enter Your name : ");
    scanf("%s",(*ptr).name);//printf("%s",(*ptr).name);
    (*ptr).ac=10+(*p);
    printf("Acount number(a/c) = %d ",(*ptr).ac);
    printf("\nPlese create a pin of 4 digites = ");
    scanf("%d",&pi);
    while(pi<999 || pi>10000)
    {
        printf("your pin is not with in 4 digites plese enter again =");
        scanf("%d",&pi);
    }
    (*ptr).pin=pi;
      do{
            printf("Plese Enter your a/c blance : ");
            scanf("%d",&(*ptr).ab);
        }while((*ptr).ab<0);
    (*p)++;
    printf("Congratulations your Acount opened !");
}
void user(struct user *ptr,int *p)
{
    int w=3,i,z,amount,pin;
    printf("Plese enter your A/C : ");
    scanf("%d",&i);
    i-=10;
    ptr+=i;
    if((*(ptr+i)).block)
    {
        printf("your name is : MR/MS %s\n",(*ptr).name);
        printf("ypur blance is : %d\n",(*ptr).ab);
          do{
                printf("For mony Withdrall enter -->0 \nFor mony Deposit enter -->1 \nplese enter -->");
                scanf("%d",&z);
            }while(!(z>-1 && z<2));
        printf("Plese Enter the amount : ");
        scanf("%d",&amount);
        printf("plese enter the pin :");
        while(w)
        {
            scanf("%d",&pin);
            if((*ptr).pin==pin)
                break;
            else
            {
                printf("you enter a wrong pin %d try's left plese enter corouct pin : ",--w);
            }

        }
        if(w)
            if(z)
            {
                (*ptr).ab+=amount;
                printf("your A/C blance is : %d",(*ptr).ab);
            }
            else
            {
            	if((*ptr).ab<amount)
            		printf("you don't have that much mony in your A/C !");
            	else
            	{
                	(*ptr).ab-=amount;
                	printf("your A/C blance is : %d",(*ptr).ab);
          		}
            }
        else
        {
            printf("your acount pin is blocked ");
            (*ptr).block=0;
        }
    }
    else
        printf("your acount is blocked plese concact bank");
}
void Administrative(struct user *ptr,int *p)
{
    int i,password=10092003,ch,pi;
    printf("plese enter the password");
    scanf("%d",&ch);
    if(ch==password)
    {
        printf("Plese enter your A/C : ");
        scanf("%d",&i);
        i-=10;
        ptr+=i;
        printf("your name is : MR/MS %s\n",(*ptr).name);
        printf("ypur blance is : %d\n",(*ptr).ab);
        printf("\n Plese create a pin of 4 digites = ");
        scanf("%d",&pi);
        while((pi<999 || pi>10000))
        {
            printf("your pin is not with in 4 digites plese enter again =");
            scanf("%d",&pi);
        }
        (*ptr).pin=pi;
        (*ptr).block=1;
    }

}
int main()
{
    int z=0,sbiu=0,pnbu=0,boiu=0,*p1;
    struct user sbi[10],pnb[10],boi[10],*p;
    void (*a[])(struct user*,int*)={opening,user,Administrative};
    do{
      do{
            printf("Plese enter 0 --> State Bank of India\nPlese enter 1 --> Panjab National Bank\nPlese enter 2 --> Bank Of India\nPlese enter -->");
            scanf("%d",&z);
        }while(!(z>-1 && z<3));
        if(!z)
    {
        p=sbi;
        p1=&sbiu;
        printf("Welcome to State Bank of India\n");
    }
    else if(z==1)
    {
        p=pnb;
        p1=&pnbu;
        printf("Welcome to Panjab National Bank\n");
    }
    else
    {
        p=boi;
        p1=&boiu;
        printf("Welcome to Bank Of India\n");
    }
      do{
            printf("Plese enter 0 --> Opening new acount\nPlese enter 1 --> User login\nPlese enter 2 -->Administrative login\nPlese enter -->");
            scanf("%d",&z);
        }while(!(z>-1 && z<3));
    a[z](p,p1);
    printf("\nplese enter 0 --> to stop\neny number --> to continue \n-->");
    scanf("%d",&z);
    }while(z);
return 0;
}
