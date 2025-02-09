async function findAnItem(string){
    console.log('Calling findAnItem...');
    let item_to_return;
    await import('./node_modules/warframe-items/utilities/find').then(
        module => {
            console.log('Calling findItem...');
            item_to_return = module.findItem(string);
            console.log('Got the item.');
            console.log(item_to_return);
        }).catch(
        error => {
            console.error('Error loading module:', error);
        }
    );
    console.log('Successfully got the item!');
    console.log(item_to_return);
    return item_to_return;
}

module.exports = {
    findAnItem
}

