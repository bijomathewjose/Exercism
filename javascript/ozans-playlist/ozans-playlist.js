// @ts-check
//
// The line above enables type checking for this file. Various IDEs interpret
// the @ts-check directive. It will give you helpful autocompletion when
// implementing this exercise.

/**
 * Removes duplicate tracks from a playlist.
 *
 * @param {string[]} playlist
 * @returns {string[]} new playlist with unique entries
 */
export function removeDuplicates(playlist) {
  const freshList=new Set();
  let size=0;
  return playlist.map(song=>{
    if(freshList.add(song).size!=size) {
      size++;
      return song;}
    })
}

/**
 * Checks whether a playlist includes a track.
 *
 * @param {string[]} playlist
 * @param {string} track
 * @returns {boolean} whether the track is in the playlist
 */
export function hasTrack(playlist, track) {
  for(let song of playlist )
    if(song===track) 
      return true
  return false
}

/**
 * Adds a track to a playlist.
 *
 * @param {string[]} playlist
 * @param {string} track
 * @returns {string[]} new playlist
 */
export function addTrack(playlist, track) {
  playlist.push(track)
  return removeDuplicates(playlist)
}

/**
 * Deletes a track from a playlist.
 *
 * @param {string[]} playlist
 * @param {string} track
 * @returns {string[]} new playlist
 */
export function deleteTrack(playlist, track) {
  playlist.map((song,index)=>{
    if(track===song){
      playlist.splice(index,1)
    }
  })
  return playlist

}

/**
 * Lists the unique artists in a playlist.
 *
 * @param {string[]} playlist
 * @returns {string[]} list of artists
 */
export function listArtists(playlist) {
const Artists=new Set();
let size=0,artist;
return playlist.map(song=>{
  artist=song.split('-')[1].trim();
  
  if( Artists.add(artist).size!=size) {
    
      size++;
    
    console.log(artist)
      return artist}
    })
}
