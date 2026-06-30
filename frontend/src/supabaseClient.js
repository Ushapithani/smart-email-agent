import { createClient } from '@supabase/supabase-js';

const supabaseUrl = 'https://hzbvghzibubvtotaxvsc.supabase.co'; // Aapka URL
const supabaseAnonKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imh6YnZnaHppYnVidnRvdGF4dnNjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODIwNTE0MzYsImV4cCI6MjA5NzYyNzQzNn0.wmgiNGNfFnvjSd-1aQqEIUsEU8XiG5Ieo2zA5kaBKxQ'; // Jo lambi string aapne pehle bheji thi

export const supabase = createClient(supabaseUrl, supabaseAnonKey);