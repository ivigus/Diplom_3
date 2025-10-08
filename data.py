class URLs:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/'
    FORGOT_PASSWORD_PAGE = 'forgot-password'
    RESET_PASSWORD_PAGE = 'reset-password'
    FEED = 'feed'


class UserCredentials:
    EMAIL = 'winchesters@ya.ru'
    PASSWORD = 'avadakadavra'
    EMAIL_TO_RECOVER_PASSWORD = 'abrakadabra123@yandex.ru'
    SOME_PASSWORD = 'testtest'


class Scripts:
    DRAG_AND_DROP_SCRIPT = """
        function simulateHTML5DragAndDrop(sourceNode, destinationNode) {
            var dataTransfer = new DataTransfer();
            var dragStartEvent = new DragEvent('dragstart', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            });
            sourceNode.dispatchEvent(dragStartEvent);
            var dropEvent = new DragEvent('drop', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            });
            destinationNode.dispatchEvent(dropEvent);

            var dragEndEvent = new DragEvent('dragend', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            });
            sourceNode.dispatchEvent(dragEndEvent);
        }
        simulateHTML5DragAndDrop(arguments[0], arguments[1]);
    """