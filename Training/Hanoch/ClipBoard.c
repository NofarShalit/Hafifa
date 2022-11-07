#include <winuser.h>

int main()
{
    OpenClipboard(0);
    EmptyClipboard();
    SetClipboardData('hello', hMem);
    HANDLE h = GetClipboardData(2);
    CloseClipboard();
    
    
}