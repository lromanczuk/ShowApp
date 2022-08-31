function requestsLogic(menu_items) {

    for (let i = 0; i < menu_items.length; ++i) {
        menu_items[i].onclick = (e)=>{
            // menu colors logic
            for (let j = 0; j < menu_items.length; ++j) {
                // clear class
                menu_items[j].classList.remove('menu-link-active')
                menu_items[j].classList.remove('no-click')

                if (menu_items[i]==menu_items[j]) {
                    menu_items[j].classList.add('no-click')
                    if (Array.from(menu_items[j].classList).includes('menu-link')) {
                        menu_items[j].classList.add('menu-link-active');
                    }
                }
                // cancel request
                else{
                    htmx.trigger(menu_items[j], 'htmx:abort')
                }  
            }
        }
    }
    }


    // pick all rquest items 

    // first run
    requestsLogic(document.getElementsByClassName('request-item'))

    // set onclick on all items when content change
    const mutationObserver_all = new MutationObserver(enteries  => {
        new_menu_items = document.getElementsByClassName('request-item');
        requestsLogic(new_menu_items)

        // get all flashs
        htmx.ajax('GET', '/flashs', '#flash')
    })

    const panel_content = document.querySelector('#panel-content')
    if (panel_content) {
        mutationObserver_all.observe(panel_content, {childList: true})
    }
    

    
