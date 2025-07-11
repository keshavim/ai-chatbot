import { Component } from '@angular/core';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule, HttpClientModule],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  userMessage = '';
  messages: { role: string; content: string }[] = [];
  loading = false;

  constructor(private http: HttpClient) {}

  sendMessage() {
    const message = this.userMessage.trim();
    if (!message) return;

    this.messages.push({ role: 'user', content: message });
    const payload = { messages: this.messages };
    this.loading = true;
    this.userMessage = '';

    this.http.post<{ content: string }>('http://localhost:5000/chat', payload).subscribe({
      next: (response) => {
        this.messages.push({ role: 'assistant', content: response.content });
        this.loading = false;
      },
      error: (err) => {
        console.error('API error', err);
        this.messages.push({ role: 'assistant', content: '[Error: Failed to reach server]' });
        this.loading = false;
      }
    });
  }
}
